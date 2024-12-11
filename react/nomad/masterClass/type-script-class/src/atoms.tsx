import { atom, selector } from "recoil";

interface IToDoState {
  [key: string]: string[];
}

export const toDoState = atom<IToDoState>({
  key: "toDo",
  default: {
    "TO DO": ["a", "d", "e"],
    Doing: ["b", "c"],
    Done: ["f"],
  },
});
