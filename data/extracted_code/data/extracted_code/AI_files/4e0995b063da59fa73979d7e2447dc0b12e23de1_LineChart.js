export default function LineChart({ book, db }) {
  let [userData, setUserData] = useState(null);

  useEffect(() => {
    const unsubscribe = onSnapshot(doc(db, book?.id), (doc) => {
      setUserData(doc.data());
    });
    return () => unsubscribe();
  }, [db, book?.id]);
  console.log(userData);

  let total_pages = book?.pages;
  const keys = userData ? Object.keys(userData) : [];
  let dates = [];
  let pages = [];
  keys.forEach((key) => dates.push(key));
  dates = dates.sort();
  dates.forEach((date) => {
    pages.push(userData[date]);
  });