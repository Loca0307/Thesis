            //! ChatGPT's parser -  Parse the page parameter
            var pageValues = Request.Query["page"].ToString();
            if (int.TryParse(pageValues, out int parsedPage) && parsedPage > 0)
            {
                CurrentPage = parsedPage;
            }
