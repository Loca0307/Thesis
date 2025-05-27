const intialState={
    cart:[],
    totalPrice:0,
    cartId:null, 
}

export const cartReducer=(state=intialState,action)=>{
    switch(action.type){
        case "ADD_CART":
            const productToAdd=action.payload;
            const exsistingProduct=state.cart.find(
                (item)=>item.productId===productToAdd.productId
            );
            if(exsistingProduct){
                const updatedCart=state.cart.map((item)=>{
                    if(item.productId===productToAdd.productId){
                        return productToAdd;
                    }
                    else{
                        return item;
                    }
                });
                return{
                    ...state,
                    cart:updatedCart,
                }
            }
            else{
                const newCart=[...state.cart,productToAdd];
                return{
                    ...state,
                    cart:newCart,
                }
            }
        default:
             return state;
    }
}