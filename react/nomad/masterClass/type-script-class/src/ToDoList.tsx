import { useForm } from "react-hook-form";
import { DefaultValue } from "recoil";

interface IForm {
    email: string
    firstName: string
    lastName: string
    username: string
    password: string
    password1: string
    extraError: string
}

function ToDoList() {
    // The handleSubmit func has reponsible for managing somthing like Preventing default, validation, etc...  
    const { register, handleSubmit, formState: { errors }, setError } = useForm<IForm>({
        defaultValues: {
            email: "@naver.com"
        }
    });
    // When it's invalid, react-hook helps us modifying in terms of user-experience
    const onValid = (data: IForm) => {
        if (data.password != data.password1) {
             setError("password1", { message: "Passwords are not the same" }, { shouldFocus: true  })
        }
         // setError("extraError", { message: "Server offline" })
    };

    return <div>
        <form style={{display: "flex", flexDirection: "column"}} onSubmit={handleSubmit(onValid)}>
            <input {...register("email", { 
                required: "Email is required", 
                pattern: { 
                        value: /^[A-Za-z0-9._%+-]+@naver.com$/, 
                        message: "Only naver.com emails allowed"
                    } 
                }
            )} placeholder="Email">
            </input>
            <span>{ errors?.email?.message as string }</span>
            <input {...register("firstName", { 
                required: "firstName is required",
                validate: {
                    noNico: (value) => value.includes("nico") ? "no nico allowed" : true,
                    noNick: (value) => value.includes("nick") ? "no nick  allowed" : true  
                },
                })}  placeholder="firstName"></input>
            <span>{ errors?.firstName?.message as string }</span>
            <input {...register("lastName", { required: "lastName is required" })}  placeholder="lastName"></input>
            <span>{ errors?.lastName?.message as string }</span>
            <input {...register("username", { required: "username is required", minLength: 10 })}  placeholder="username"></input>
            <span>{ errors?.username?.message as string }</span>
            <input {...register("password", { required: "Password is required", minLength: { value: 5, message: "Your password very short"} })}  placeholder="password"></input>
            <span>{ errors?.password?.message as string }</span>
            <input {...register("password1", { required: "Password1 is required", minLength: { value: 5, message: "Your password very short"} })}  placeholder="password1"></input>
            <span>{ errors?.password1?.message as string }</span>
            <button >Add</button>
            <span>{ errors?.extraError?.message as string }</span>
        </form>
    </div>;
}

export default ToDoList;
