package simulation;

import base.SessionId;
import io.gatling.javaapi.core.*;
import io.gatling.javaapi.http.HttpProtocolBuilder;

import java.time.Duration;
import java.util.concurrent.ThreadLocalRandom;

import static io.gatling.javaapi.core.CoreDsl.*;
import static io.gatling.javaapi.http.HttpDsl.*;

public class SimulationDemoStore4UserJourneys extends Simulation {
    private static final String DOMAIN = "demostore.gatling.io";
    private static final HttpProtocolBuilder HTTP_PROTOCOL = http.baseUrl("https://" + DOMAIN);
    private static final int USER_COUNT = Integer.parseInt(System.getProperty("USERS", "5"));
    private static final Duration RAMP_DURATION = Duration.ofSeconds(Integer.parseInt(System.getProperty("RAMP_DURATION", "10")));
    private static final Duration TEST_DURATION = Duration.ofSeconds(Integer.parseInt(System.getProperty("TEST_DURATION", "60")));
    private static final FeederBuilder<String> csvFeederCategoryFeeder = csv("data/categoryDetails.csv").circular();
    private static final FeederBuilder<Object> jsonFeederProductFeeder = jsonFile("data/productDetails.json").random();
    private static final FeederBuilder<String> csvFeederLoginDetails = csv("data/loginDetails.csv").circular();
    private static final ChainBuilder initSession =
            exec(flushCookieJar())
                    .exec(session -> session.set("randomNumber", ThreadLocalRandom.current().nextInt()))
                    .exec(session -> session.set("customerLoggedIn", false))
                    .exec(session -> session.set("cartTotal", 0))
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
                                    .check(substring("items in your cart")))
                            .exec(session -> {
                                double currentCartTotal = session.getDouble("cartTotal");
                                double itemPrice = session.getDouble("price");
                                return session.set("cartTotal", currentCartTotal + itemPrice);
                            })
                            .exec(
                                    session -> {
                                        System.out.println("Cart Total : " + session.get("cartTotal").toString());
                                        return session;
                                    }
                            );
            ;
        }
    }

    private static class Customer {
        private static final ChainBuilder login =
                feed(csvFeederLoginDetails)
                        .exec(http("Load Login Page for #{username}")
                                .get("/login")
                                .check(substring("Username:")))
                        .exec(
                                session -> {
                                    System.out.println("Customer logged in: " + session.get("customerLoggedIn").toString());
                                    return session;
                                }
                        )
                        .exec(http("Customer Login Action with #{username}")
                                .post("/login")
                                .formParam("_csrf", "#{csrfValue}")
                                .formParam("username", "#{username}")
                                .formParam("password", "#{password}"))
                        .exec(session -> session.set("customerLoggedIn", true))
                        .exec(
                                session -> {
                                    System.out.println("Customer logged in: " + session.get("customerLoggedIn").toString());
                                    return session;
                                }
                        );
    }

    private static class Checkout {
        private static final ChainBuilder viewCart =
                doIf(session -> !session.getBoolean("customerLoggedIn"))
                        .then(exec(Customer.login))
                        .exec(http("View Cart")
                                .get("/cart/view")
//                                .check(css("#grandTotal").isEL("$#{cartTotal}"))
                        );
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
            .exec(Checkout.checkout)
            .pause(3);
    private static class UserJourneys {
        private static final Duration MIN_PAUSE = Duration.ofMillis(100);
        private static final Duration MAX_PAUSE = Duration.ofMillis(500);
        private static final ChainBuilder browseStore =
                exec(initSession)
                        .exec(CmsPage.homePage)
                        .pause(MAX_PAUSE)
                        .exec(CmsPage.aboutUs)
                        .pause(MIN_PAUSE,MAX_PAUSE)
                        .repeat(5)
                        .on(
                                exec(Catalog.Category.view)
                                        .pause(MIN_PAUSE,MAX_PAUSE)
                                        .exec(Catalog.Product.view)
                        );
        private static final ChainBuilder abandonCart =
                initSession
                        .exec(CmsPage.homePage)
                        .pause(MAX_PAUSE)
                        .exec(Catalog.Category.view)
                        .pause(MIN_PAUSE,MAX_PAUSE)
                        .exec(Catalog.Product.view)
                        .pause(MIN_PAUSE,MAX_PAUSE)
                        .exec(Catalog.Product.addProductToCart);
        private static final ChainBuilder completePurchase =
                initSession
                        .exec(CmsPage.homePage)
                        .pause(MAX_PAUSE)
                        .exec(Catalog.Category.view)
                        .pause(MIN_PAUSE,MAX_PAUSE)
                        .exec(Catalog.Product.view)
                        .pause(MIN_PAUSE,MAX_PAUSE)
                        .exec(Catalog.Product.addProductToCart)
                        .pause(MIN_PAUSE,MAX_PAUSE)
                        .exec(Checkout.viewCart)
                        .pause(MIN_PAUSE,MAX_PAUSE)
                        .exec(Checkout.checkout);
    }
    private static class Scenarios {
        private static final ScenarioBuilder defaultPurchase =
                scenario("Default Load Test")
                        .during(TEST_DURATION)
                        .on(
                                randomSwitch().on(
                                        Choice.withWeight(75.0,exec(UserJourneys.browseStore)),
                                        Choice.withWeight(15.0,exec(UserJourneys.abandonCart)),
                                        Choice.withWeight(10.0,exec(UserJourneys.completePurchase))
                                )
                        );
        private static final ScenarioBuilder highPurchase =
                scenario("High Purchase Load Test")
                        .during(Duration.ofSeconds(60))
                        .on(
                                randomSwitch().on(
                                        Choice.withWeight(25.0,exec(UserJourneys.browseStore)),
                                        Choice.withWeight(25.0,exec(UserJourneys.abandonCart)),
                                        Choice.withWeight(50.0,exec(UserJourneys.completePurchase))
                                )
                        );
    }

    {
        setUp(
                Scenarios.defaultPurchase.injectOpen(
                        rampUsers(USER_COUNT).during(RAMP_DURATION))
                        .protocols(HTTP_PROTOCOL)
                );
    }
}