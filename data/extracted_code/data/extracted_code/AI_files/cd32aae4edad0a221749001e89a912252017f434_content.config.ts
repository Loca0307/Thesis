---
interface Props {
  id?: string;
  mapping?: string;
}

const { 
  id = "comments",
  mapping = "pathname"
} = Astro.props;

const initialTheme = "preferred_color_scheme"; 
---

<div id={id} class="giscus-container">
    <script src="https://giscus.app/client.js"
        data-repo="grumpycatyo-collab/max-plamadeala.com"
        data-repo-id="R_kgDOOhpI6g"
        data-category="General"
        data-category-id="DIC_kwDOOhpI6s4CptT6"
        data-mapping="pathname"
        data-strict="0"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="bottom"
        data-theme={initialTheme}
        data-lang="en"
        data-loading="lazy"
        crossorigin="anonymous"
        async>
    </script>
</div>
