import { atom } from "recoil";

export const isDarkAtom = atom({
    key: "isDark", // Should be unique
    default: true
});
