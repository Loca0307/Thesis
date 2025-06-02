// // import logo from './logo.svg';
// // import './App.css';
import OrderStatusHistory from './client/orderstatus';
// // import '../client/Onboarding.jsx';
import ClientOnboarding from './client/onboarding.jsx';
import OrderRequest from './client/orderrequest.jsx';
// function App() {
//   return (
//     <div className="App">
//       {/* <ClientOnboarding></ClientOnboarding> */}
//       {/* <OrderRequest></OrderRequest> */}
//       <OrderStatusHistory></OrderStatusHistory>
//     </div>
//   );
// }

// export default App;


// import React from 'react';
// import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';


// const App = () => {
//   return (
//     <Router>
//       <nav style={{ padding: '1rem', borderBottom: '1px solid #ccc', width:'100%' }}>
//         <Link to="/" style={{ marginRight: '1rem' }}>Home</Link>
//         <Link to="/order-request">Order Request</Link>
//         <Link to="/order-status">Order Status</Link>

//       </nav>
//       <Routes>
//         <Route path="/" element={<ClientOnboarding />} />
//         <Route path="/order-request" element={<OrderRequest />} />
//         <Route path="/order-status" element={<OrderStatusHistory />} />

//       </Routes>
//     </Router>
//   );
// };

// export default App;


import React from "react";
import { BrowserRouter as Router, Routes, Route, BrowserRouter } from "react-router-dom";
import Sidebar from './navigation/sidebar.jsx';

const App = () => {
  return (
  
    <BrowserRouter basename='{process.env.PUBLIC_URL}'>
      <div style={{ display: "flex" }}>
        <Sidebar />
        <div style={{ marginLeft: "250px", flex: 1, padding: "1rem" }}>
          <Routes>
            <Route path="/" element={<ClientOnboarding></ClientOnboarding>} />
            <Route path="/order-request" element={<OrderRequest></OrderRequest>} />
            <Route path="/order-status" element={<OrderStatusHistory></OrderStatusHistory>} />
            {/* <Route path="/customers" element={<h1>Customers</h1>} />
            <Route path="/reports" element={<h1>Reports</h1>} />
            <Route path="/settings" element={<h1>Settings</h1>} /> */}
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
};

export default App;