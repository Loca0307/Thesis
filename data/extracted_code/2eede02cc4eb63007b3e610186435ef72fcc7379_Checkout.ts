import { expect, Locator, Page } from "@playwright/test";
import { PageBase } from "./PageBase";
import { Address, CheckoutProduct } from "../models/CheckoutModels";
import { User } from "../models/UserModels";
import { Product } from "../models/ProductModels";

export class Checkout extends PageBase {
    // Locators
    deliveryAddressSection: Locator;
    billingAddressSection: Locator;
    productRows: Locator;
    commentTextarea: Locator;
    placeOrderButton: Locator;
    totalAmount: Locator;

    constructor(page: Page) {
        super(page);

        this.url = "/checkout";
        this.title = "Automation Exercise - Checkout";
        this.logo = "//div[contains(@class,'logo')]";

        this.deliveryAddressSection = page.locator("#address_delivery");
        this.billingAddressSection = page.locator("#address_invoice");
        this.productRows = page.locator("tr[id^='product-']");
        this.commentTextarea = page.locator("#ordermsg textarea");
        this.placeOrderButton = page.locator(".check_out");
        this.totalAmount = page.locator(".cart_total_price").last();
    }

    /**
     * Get delivery address details
     * @returns Address object with delivery information
     */
    async getDeliveryAddress(): Promise<Address> {
        await expect(this.deliveryAddressSection).toBeVisible();
        
        const fullName = await this.deliveryAddressSection.locator(".address_firstname.address_lastname").textContent() || "";
        
        // Get address lines (skipping empty ones)
        const addressLinesElements = this.deliveryAddressSection.locator(".address_address1.address_address2");
        const addressLinesCount = await addressLinesElements.count();
        const addressLines: string[] = [];
        
        for (let i = 0; i < addressLinesCount; i++) {
            const lineText = await addressLinesElements.nth(i).textContent() || "";
            if (lineText.trim()) {
                addressLines.push(lineText.trim());
            }
        }
        
        const cityStatePostcode = await this.deliveryAddressSection.locator(".address_city.address_state_name.address_postcode").textContent() || "";
        const country = await this.deliveryAddressSection.locator(".address_country_name").textContent() || "";
        const phone = await this.deliveryAddressSection.locator(".address_phone").textContent() || "";
        
        return {
            fullName,
            addressLines,
            cityStatePostcode,
            country,
            phone
        };
    }

    /**
     * Get billing address details
     * @returns Address object with billing information
     */
    async getBillingAddress(): Promise<Address> {
        await expect(this.billingAddressSection).toBeVisible();
        
        const fullName = await this.billingAddressSection.locator(".address_firstname.address_lastname").textContent() || "";
        
        // Get address lines (skipping empty ones)
        const addressLinesElements = this.billingAddressSection.locator(".address_address1.address_address2");
        const addressLinesCount = await addressLinesElements.count();
        const addressLines: string[] = [];
        
        for (let i = 0; i < addressLinesCount; i++) {
            const lineText = await addressLinesElements.nth(i).textContent() || "";
            if (lineText.trim()) {
                addressLines.push(lineText.trim());
            }
        }
        
        const cityStatePostcode = await this.billingAddressSection.locator(".address_city.address_state_name.address_postcode").textContent() || "";
        const country = await this.billingAddressSection.locator(".address_country_name").textContent() || "";
        const phone = await this.billingAddressSection.locator(".address_phone").textContent() || "";
        
        return {
            fullName,
            addressLines,
            cityStatePostcode,
            country,
            phone
        };
    }

    /**
     * Get product information by index
     * @param index The index of the product (0-based)
     * @returns CheckoutProduct object with product details
     */
    async getProductInfo(index: number): Promise<CheckoutProduct> {
        const productRow = this.productRows.nth(index);
        await expect(productRow).toBeVisible();
        
        const id = (await productRow.getAttribute("id") || "").replace("product-", "");
        const name = await productRow.locator(".cart_description h4 a").textContent() || "";
        const category = await productRow.locator(".cart_description p").textContent() || "";
        const price = await productRow.locator(".cart_price p").textContent() || "";
        const quantity = await productRow.locator(".cart_quantity button").textContent() || "";
        const total = await productRow.locator(".cart_total p").textContent() || "";
        
        return {
            id:Number(id),
            name,
            category,
            price:Number(price),
            quantity:Number(quantity),
            availability: "",
            condition: "",
            brand: "",
            total
        };
    }

    /**
     * Get product information by product ID
     * @param name The ID of the product
     * @returns CheckoutProduct object with product details
     */
    async getProductByName(productName: string): Promise<CheckoutProduct> {
        const productRow = this.page.locator(`//a[contains(text(),"${productName}")]//ancestor::tr`);
        
        if (await productRow.count() === 0) {
            console.log(`Product with name "${productName}" not found in the checkout.`);
        }
        
        await expect(productRow).toBeVisible();
        
        const id = (await productRow.getAttribute("id") || "").replace("product-", "");
        const name = await productRow.locator(".cart_description h4 a").textContent() || "";
        const category = await productRow.locator(".cart_description p").textContent() || "";
        const price = await productRow.locator(".cart_price p").textContent() || "";
        const quantity = await productRow.locator(".cart_quantity button").textContent() || "";
        const total = await productRow.locator(".cart_total p").textContent() || "";
        
        return {
            id: Number(id),
            name,
            category,
            price: Number(price),
            quantity: Number(quantity),
            availability: "",
            condition: "",
            brand: "",
            total
        };
    }

    async verifyDeliveryAddress(user: User) {
        const deliveryAddress = await this.getDeliveryAddress();

        expect(deliveryAddress.fullName).toContain(user.name);
        expect(deliveryAddress.addressLines[0]).toContain(user.addressInfo.firstName);
        expect(deliveryAddress.cityStatePostcode).toContain(user.addressInfo.city);
        expect(deliveryAddress.country).toContain(user.addressInfo.country);
        expect(deliveryAddress.phone).toContain(user.addressInfo.mobile);

        return this;
    }

    async verifyBillingAddress(user: User) {
        const billingAddress = await this.getBillingAddress();

        expect(billingAddress.fullName).toContain(user.name);
        expect(billingAddress.addressLines[0]).toContain(user.addressInfo.firstName);
        expect(billingAddress.cityStatePostcode).toContain(user.addressInfo.city);
        expect(billingAddress.country).toContain(user.addressInfo.country);
        expect(billingAddress.phone).toContain(user.addressInfo.mobile);

        return this;
    }

    async verifyProductInfo(product: Product) {
        const productInfo = await this.getProductByName(product.name);

        expect(productInfo.name).toEqual(product.name);
        expect(productInfo.category).toEqual(product.category);
        expect(productInfo.price).toEqual(`Rs. ${product.price}`);
        expect(productInfo.quantity).toEqual(product.quantity);
        expect(productInfo.total).toEqual(`Rs. ${product.price * product.quantity}`);

        return this;
    }

    /**
     * Get all products in the checkout
     * @returns Array of CheckoutProduct objects
     */
    async getAllProducts(): Promise<CheckoutProduct[]> {
        const products: CheckoutProduct[] = [];
        const count = await this.productRows.count();
        
        for (let i = 0; i < count; i++) {
            products.push(await this.getProductInfo(i));
        }
        
        return products;
    }

    /**
     * Add a comment to the order
     * @param comment The text to add as a comment
     */
    async addComment(comment: string) {
        await expect(this.commentTextarea).toBeVisible();
        await this.commentTextarea.fill(comment);
        return this;
    }

    /**
     * Place the order by clicking the Place Order button
     */
    async placeOrder() {
        await expect(this.placeOrderButton).toBeVisible();
        await this.placeOrderButton.click();
        await this.page.waitForLoadState('networkidle');
        return this;
    }

    /**
     * Get the total amount of the order
     * @returns The total amount as a string
     */
    async getTotalAmount(): Promise<string> {
        return await this.totalAmount.textContent() || "";
    }
}