import { ReactNode, useEffect, useState } from "react";
import { DataContext } from "./DataContext";
import { useStreamingFetch } from "./hooks/useStreamingFetch";
import { DataContextType, LogItemDataWithId } from "./type";

/**
 * DataProvider component that fetches log data from a given URL and provides it to its children.
 * It uses the useStreamingFetch hook to handle the fetching logic.
 *
 * @param {ReactNode} children - The child components that will have access to the fetched data.
 * @param {string} url - The URL from which to fetch the log data. Defaults to a specific S3 URL.
 */
export const DataProvider: React.FC<{ children: ReactNode; url?: string }> = ({
  children,
  url = "https://s3.amazonaws.com/io.cribl.c021.takehome/cribl.log",
}) => {
  // TODO: Add delayBetweenRead to the useStreamingFetch hook
  // TODO: Use requestIdleCallback to parse the data when the items is not empty
  // TODO: Add useDeferredValue to the items state
  const [items, setItmes] = useState<DataContextType["items"]>([]);
  const [parsedIndex, setParsedIndex] = useState(0);

  const { data, loading, error, lastModified, refetch } = useStreamingFetch(url);

  useEffect(() => {
    if (parsedIndex < data.length) {
      const newItems = data
        .slice(parsedIndex)
        .map((item, index): LogItemDataWithId | null => {
          try {
            return {
              data: JSON.parse(item),
              id: `${lastModified}-${index + parsedIndex}`,
            };
          } catch {
            return null;
          }
        })
        .filter(Boolean) as LogItemDataWithId[];
      setItmes((prev) => [...prev, ...newItems]);
      setParsedIndex(data.length);
    }
  }, [data, lastModified, parsedIndex]);

  const value: DataContextType = {
    items,
    loading,
    error,
    refetch,
  };
  return <DataContext.Provider value={value}>{children}</DataContext.Provider>;
};