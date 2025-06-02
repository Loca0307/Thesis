package perf;

import io.gatling.javaapi.core.ChainBuilder;
import io.gatling.javaapi.core.FeederBuilder;
import io.gatling.javaapi.core.ScenarioBuilder;
import io.gatling.javaapi.core.Simulation;
import io.gatling.javaapi.http.HttpProtocolBuilder;

import java.util.concurrent.ThreadLocalRandom;

import static io.gatling.javaapi.core.CoreDsl.*;
import static io.gatling.javaapi.http.HttpDsl.*;

public class RecordedSimulationDemoStore1Refactored6Sessions extends Simulation {
    private static final String DOMAIN = "demostore.gatling.io";
    private static final HttpProtocolBuilder HTTP_PROTOCOL = http.baseUrl("https://" + DOMAIN);
    private static final FeederBuilder<String> csvFeederCategoryFeeder = csv("data/categoryDetails.csv").circular();
    private static final FeederBuilder<Object> jsonFeederProductFeeder = jsonFile("data/productDetails.json").random();
    private static final FeederBuilder<String> csvFeederLoginDetails = csv("data/loginDetails.csv").circular();
    private static final ChainBuilder initSession =
            exec(flushCookieJar())
                    .exec(session -> session.set("randomNumber", ThreadLocalRandom.current().nextInt()))
                    .exec(session -> session.set("customerLoggedIn",false))
                    .exec(session -> session.set("cartTotal",0))
                    .exec(addCookie(Cookie("sessionID", SessionId.random()).withDomain(DOMAIN)));

    private static class CmsPage {
        private static final ChainBuilder homePage =
                exec(http("Load Home Page")
                        .get("/")
                        .check(css("#_csrf", "content").saveAs("csrfValue"))
                        .check(regex("<title>Gatling Demo-Store</title>").exists()));
        private static final ChainBuilder aboutUs =
                exec(http("Load About Us Page")
                        .get("/about-us")
                        .check(substring("About Us")));
    }

    private static class Catalog {
        private static class Category {
            private static final ChainBuilder view =
                    feed(csvFeederCategoryFeeder)
                            .repeat(2, "n").on(
                                    exec(http("View #{n} Category - #{categoryName}")
                                            .get("/category/#{categorySlug}")
                                            .check(css("#CategoryName").isEL("#{categoryName}")))); // EL = Expression Language
        }

        private static class Product {
            private static final ChainBuilder view =
                    feed(jsonFeederProductFeeder)
                            .exec(http("View Product - #{name}")
                                            .get("/product/#{slug}")
                                            .check(css("#ProductDescription").isEL("#{description}")));
            private static final ChainBuilder addProductToCart =
                    exec(view)
                            .exec(http("Add to Cart - ${name}")
                                    .get("/cart/add/${id}")
                                    .check(substring("items in your cart")));
        }
    }
    private static class Customer {
        private static final ChainBuilder login =
                feed(csvFeederLoginDetails)
                        .exec(http("Load Login Page for #{username}")
                                .get("/login")
                                .check(substring("Username:")))
                        .exec(http("Customer Login Action with #{username}")
                                .post("/login")
                                .formParam("_csrf", "#{csrfValue}")
                                .formParam("username", "#{username}")
                                .formParam("password", "#{password}"));
    }
    private static class Checkout {
        private static final ChainBuilder viewCart =
                exec(http("View Cart")
                        .get("/cart/view"));
        private static final ChainBuilder checkout =
                        exec(http("Checkout")
                                .get("/cart/checkout")
                                .check(substring("Thanks for your order! See you soon!")));
    }

    private static final ScenarioBuilder scn = scenario("RecordedSimulationDemoStore1")
            .exec(initSession)
            .exec(CmsPage.homePage)
            .pause(2)
            .exec(CmsPage.aboutUs)
            .pause(2)
            .exec(Catalog.Category.view)
            .pause(2)
            .exec(Catalog.Product.addProductToCart)
            .pause(2)
            .exec(Checkout.viewCart)
            .pause(3)
            .exec(Customer.login)
            .pause(2)
            .exec(Checkout.checkout)
            .pause(3)
            ;

    {
        setUp(scn.injectOpen(atOnceUsers(4))).protocols(HTTP_PROTOCOL);
    }
}