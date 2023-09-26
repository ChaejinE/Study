import { Table } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import { increaseOne } from "../store/itemSlice";

function Cart() {
    let items = useSelector((state) => { return state.items });
    let dispatch = useDispatch();

    return (
        <div>
            <Table>
                <thead>
                    <tr>
                    <th>#</th>
                    <th>상품명</th>
                    <th>수량</th>
                    <th>변경하기</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        items.map((item, idx) => {
                            return (
                                <tr key={idx}>
                                <td>{item.id}</td>
                                <td>{item.name}</td>
                                <td>{item.count}</td>
                                <td>
                                    <button onClick={() => {
                                        dispatch(increaseOne(item.id));
                                    }}>+</button>
                                </td>
                                </tr>
                            )
                        })
                    }
                    
                </tbody>
            </Table>
        </div>
    )
}

export default Cart;