import { createSlice } from "@reduxjs/toolkit";

let items = createSlice({
    name: "items",
    initialState: [],
    reducers : {
        increaseOne(state, action) {
            let id = action.payload;
            let idx = state.findIndex((elem) => {return elem.id === id});
            state[idx].count++;
        },
        addInCart(state, action) {
            let item = action.payload;
            let isExsit = state.find((elem) => {return item.id === elem.id});

            if (!isExsit) {
                item = {id: item.id, name: item.title, price: item.price, count: 1,};
                state.push(item);
            }
        }
    }
})

export let { increaseOne, addInCart } = items.actions
export default items
