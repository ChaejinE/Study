import { useState, useEffect } from "react";
import style from "./tab.module.css"
import { cleanup } from "@testing-library/react";

function TabContent({tab}) {
    let contents = [
        <div> 내용 0 </div>,
        <div> 내용 1 </div>,
        <div> 내용 2 </div>
    ]
    let [fade, setFade] = useState('');

    useEffect(() => {
        let timer1 = setTimeout(() => {
                            setFade(style.end);
                        }, 10);

        return () => {
            cleanup(timer1);
            setFade('');
        }
    }, [tab])
    
    // let result = null
    // if (tab == 0) {
    //     result = <div> 내용 0 </div>
    // } else if (tab == 1) {
    //     result = <div> 내용 1 </div>
    // } else {
    //     result = <div> 내용 2 </div>
    // }

    return (
        <div className={`${style.start} ${fade}`}>
            {
                contents[tab]
            }
        </div>
    );
}

export default TabContent