import { useParams } from "react-router-dom"
import { useEffect, useState } from "react";
import { Nav } from "react-bootstrap"

function Detail(props) {
    let { id } = useParams();
    let shoe = props.shoes.filter((shoe) => {
        return shoe.id == id; 
    })[0]
    let [alert, setAlert] = useState(false);
    let [isNumber, setIsNumber] = useState(true);
    let [tab, setTab] = useState(0);

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

            <Nav onClick={(e) => { 
                let eventKey = e.target.dataset.rrUiEventKey;
                let index = eventKey.replace("link", "");
                setTab(parseInt(index));
                }} variant="tabs"  defaultActiveKey="link0">
                <Nav.Item>
                    <Nav.Link eventKey="link0">버튼0</Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link eventKey="link1">버튼1</Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link eventKey="link2">버튼2</Nav.Link>
                </Nav.Item>
            </Nav>

            <TabContent tab={tab}/>
        </div> 
    )
}

function TabContent({tab}) {
    let contents = [
        <div> 내용 0 </div>,
        <div> 내용 1 </div>,
        <div> 내용 2 </div>
    ]
    // let result = null
    // if (tab == 0) {
    //     result = <div> 내용 0 </div>
    // } else if (tab == 1) {
    //     result = <div> 내용 1 </div>
    // } else {
    //     result = <div> 내용 2 </div>
    // }

    return contents[tab];
}
export default Detail