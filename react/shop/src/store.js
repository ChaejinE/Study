import { configureStore } from "@reduxjs/toolkit";
import items from "./store/itemSlice"

export default configureStore({
    reducer: {
        items: items.reducer
    }
})