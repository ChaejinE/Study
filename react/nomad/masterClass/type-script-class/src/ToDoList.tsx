import React, { useState } from "react";

function ToDoList() {
    const [toDo, setValue] = useState("");
    const onChange = (event: React.FormEvent<HTMLInputElement>) => {
        const {currentTarget : { value }} = event;
        setValue(value);
    };
    const onSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        console.log(toDo);
    }

    return <div>
        <form action="" onSubmit={onSubmit}>
            <input onChange={onChange} value={toDo} placeholder="Write a to do"></input>
            <button>Add</button>
        </form>
    </div>;
}

export default ToDoList;
