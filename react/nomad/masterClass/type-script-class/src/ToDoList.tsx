import { useForm } from "react-hook-form";

function ToDoList() {
    // The handleSubmit func has reponsible for managing somthing like Preventing default, validation, etc...  
    const { register, handleSubmit, formState }= useForm();
    // When it's invalid, react-hook helps us modifying in terms of user-experience
    const onValid = (data: any) => {
        console.log(data);
    };
    console.log(formState.errors)

    return <div>
        <form style={{display: "flex", flexDirection: "column"}} onSubmit={handleSubmit(onValid)}>
            <input {...register("Email", { required: true })}  placeholder="Email"></input>
            <input {...register("firstName", { required: true })}  placeholder="firstName"></input>
            <input {...register("lastName", { required: true })}  placeholder="lastName"></input>
            <input {...register("username", { required: true, minLength: 10 })}  placeholder="username"></input>
            <input {...register("password", { required: "Password is required", minLength: { value: 5, message: "Your password very short"} })}  placeholder="password"></input>
            <button >Add</button>
        </form>
    </div>;
}

export default ToDoList;
