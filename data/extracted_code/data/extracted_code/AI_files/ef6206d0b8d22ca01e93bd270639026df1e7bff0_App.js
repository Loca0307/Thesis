    hover: "#5c6bc0",
  },
  gradient: {
    default: "linear-gradient(to right, #43cea2, #185a9d)",
    hover: "linear-gradient(to right, #185a9d, #43cea2)",
  },
};

// Styled components
const Container = styled.div`
  background-image: url(${backgroundImage});
  background-size: cover;
  background-position: center;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #ffffff;
  font-family: 'Arial', sans-serif;
  padding: 20px;
`;

const ButtonWrapper = styled.div`
  background-color: rgba(255, 255, 255, 0.8);  /* Semi-transparent white */
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
`;