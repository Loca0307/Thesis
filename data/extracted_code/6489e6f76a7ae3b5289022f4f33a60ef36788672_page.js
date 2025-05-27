// app/cookie-policy/page.js
import styles from "./cookiePolicy.module.css";

const CookiePolicy = () => {
  return (
    <div className={styles.container}>
      <h1 className={styles.heading1}>Cookie Policy</h1>
      <p className={styles.paragraph}>
        <strong>Last Updated:</strong> January 21, 2025
      </p>

      <h2 className={styles.heading2}>1. Introduction</h2>
      <p className={styles.paragraph}>
        Hi there! I'm a solo developer, and I run this website as a personal
        project. This Cookie Policy is here to let you know what cookies I use
        on this site, why I use them, and how they help the website function.
        Since I only use essential cookies, there’s nothing to worry about —
        they’re necessary for the website to work properly.
      </p>
      <p className={styles.paragraph}>
        By continuing to browse this site, you agree to the use of these
        cookies.
      </p>

      <h2 className={styles.heading2}>2. What Are Cookies?</h2>
      <p className={styles.paragraph}>
        Cookies are small text files that are stored on your device when you
        visit a website. They help websites remember certain information about
        your visit, like preferences or login status, so the site can work as
        expected.
      </p>

      <h2 className={styles.heading2}>3. Cookies I Use</h2>
      <p className={styles.paragraph}>
        This site uses <strong>only essential cookies</strong>. These cookies
        are needed for the website to function and cannot be disabled in the
        system. They are used for things like:
      </p>
      <ul className={styles.list}>
        <li className={styles.listItem}>
          <strong>Session management:</strong> Keeping you logged in while you
          use the site.
        </li>
      </ul>
      <p className={styles.paragraph}>
        Since these cookies are essential, they don't require your consent, but
        I want to make sure you're aware of them.
      </p>

      <h2 className={styles.heading2}>4. Why Do I Use These Cookies?</h2>
      <p className={styles.paragraph}>I use essential cookies to:</p>
      <ul className={styles.list}>
        <li className={styles.listItem}>
          Ensure the site works correctly (e.g., so you can log in or return as
          a guest).
        </li>
        <li className={styles.listItem}>
          Maintain your session while you’re using the site so that you don’t
          have to log in repeatedly.
        </li>
      </ul>
      <p className={styles.paragraph}>
        These cookies are crucial for the website’s operation and make sure the
        basic functionality is there.
      </p>

      <h2 className={styles.heading2}>5. How to Control Cookies</h2>
      <p className={styles.paragraph}>
        Since the cookies I use are essential, they are required for the website
        to function. There’s no need to accept them manually. However, if you
        prefer, you can adjust your browser settings to block or delete cookies,
        but this may affect the site’s functionality.
      </p>
      <p className={styles.paragraph}>
        Here’s how you can manage cookies in your browser:
      </p>
      <ul className={styles.list}>
        <li className={styles.listItem}>
          <a
            href="https://support.google.com/chrome/answer/95647?hl=en"
            target="_blank"
            className={styles.link}
            rel="noopener noreferrer"
          >
            Google Chrome
          </a>
        </li>
        <li className={styles.listItem}>
          <a
            href="https://support.mozilla.org/en-US/kb/enable-and-disable-cookies-website-preferences"
            target="_blank"
            className={styles.link}
            rel="noopener noreferrer"
          >
            Mozilla Firefox
          </a>
        </li>
        <li className={styles.listItem}>
          <a
            href="https://support.apple.com/guide/safari/manage-cookies-and-website-data-sfri11471/mac"
            target="_blank"
            className={styles.link}
            rel="noopener noreferrer"
          >
            Safari
          </a>
        </li>
      </ul>

      <h2 className={styles.heading2}>6. Changes to This Cookie Policy</h2>
      <p className={styles.paragraph}>
        Since this website is a personal project, I may update this policy
        occasionally. If I make any changes, I’ll update the “Last Updated” date
        above. Feel free to check back here to stay informed.
      </p>

      <h2 className={styles.heading2}>7. Contact Me</h2>
      <p className={styles.paragraph}>
        If you have any questions or concerns about this Cookie Policy or how
        cookies are used on this site, feel free to reach out to me at{" "}
        <strong className={styles.strong}>support@itsthenikolai.com</strong>.
      </p>
    </div>
  );
};

export default CookiePolicy;