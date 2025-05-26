            
            if self.config['use_page_titles']:
                title = page.meta.get('title', unquote(part))
            else:
                title = unquote(part)
                
            breadcrumbs.append(f"[{title}]({crumb_url})")
            self.logger.debug(f'Added breadcrumb: {title} with URL: {crumb_url}')