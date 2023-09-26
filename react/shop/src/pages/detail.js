import { useParams } from "react-router-dom"
import { useEffect, useState } from "react";

function Detail(props) {
    let { id } = useParams();
    let shoe = props.shoes.filter((shoe) => {
        return shoe.id == id; 
    })[0]
    let [alert, setAlert] = useState(true);
    id = parseInt(id);

    useEffect(() => {
        let timer = setTimeout(() => {
                        setAlert(false);
                    }, 2000);

        return () => {
            /* code */
            clearTimeout(timer);
        }
    }, [])

    return (
        <div className="container">
            {
                alert ? <div className="alert alert-warning">2초 후 사라진다.</div> : null
            }
            <div className="row">
                <div className="col-md-6">
                <img src={`https://codingapple1.github.io/shop/shoes${shoe.id+1}.jpg`} width="100%" />
                </div>
                <div className="col-md-6">
                <h4 className="pt-5">{shoe.title}</h4>
                <p>{shoe.content}</p>
                <p>{shoe.price}</p>
                <button className="btn btn-danger">주문하기</button> 
                </div>
            </div>
        </div> 
    )
}

export default Detail