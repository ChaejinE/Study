import { useParams } from "react-router-dom"
import { useEffect, useState } from "react";

function Detail(props) {
    let { id } = useParams();
    let shoe = props.shoes.filter((shoe) => {
        return shoe.id == id; 
    })[0]
    let [alert, setAlert] = useState(false);
    let [isNumber, setIsNumber] = useState(true);
    id = parseInt(id);

    useEffect(() => {
        setAlert(!isNumber);
    }, [isNumber])

    return (
        <div className="container">
            <div className="row">
                <div className="col-md-6">
                    <img src={`https://codingapple1.github.io/shop/shoes${shoe.id+1}.jpg`} width="100%" />
                </div>
                <div className="col-md-6">
                    <h4 className="pt-5">{shoe.title}</h4>
                    <p>{shoe.content}</p>
                    <p>{shoe.price}</p>
                    <button className="btn btn-danger">주문하기</button>
                    <div style={{marginTop: "4px"}}>
                        {
                            alert ? <div className="alert alert-warning">숫자만 쓰세요</div> : null
                        }
                        <input type="text" onInput={(e) => { 
                            let content = e.currentTarget.value;
                            let isNumber = !isNaN(Number(content));
                            setIsNumber(isNumber);
                        }}/>
                    </div>
                </div>
            </div>
        </div> 
    )
}

export default Detail