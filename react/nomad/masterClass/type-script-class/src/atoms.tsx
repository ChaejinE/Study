import { atom } from "recoil";

export interface IToDo {
    text: string;
    category: "TO_DO" | "DOING" | "DONE"; // restrcit of string
    id: number;
}

export const toDoState = atom<IToDo[]>({
    key: "toDo", 
    default: []
});
