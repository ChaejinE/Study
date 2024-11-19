import { useQuery } from "react-query";
import { fetchCoinHistory } from "../api";
import ApexChart from "react-apexcharts";
 
interface IChart {
    coinId: string;  
}

interface IHistorical {
    time_open: number;
    time_close: number;
    open: string;
    high: string;
    low: string;
    close: string;
    volume: string;
    market_cap: number;
}

function Chart({ coinId }: IChart) {
    const { isLoading, data } = useQuery<IHistorical[]>(["ohlcv", coinId], () => fetchCoinHistory(coinId));
    return (
        <>
            { isLoading ? "Loading chart..." : <ApexChart type="line" 
              series={[
                {
                  name: "Price",
                  data: data?.map(price => parseFloat(price.close)) ?? [] // or as number[]
                }
              ]}
              options={
                {
                  theme: { mode: "dark" },
                  chart: { height: 300, width: 300, toolbar: { show: false }, background: "transparent"},
                  stroke: { curve: "smooth", width: 3 },
                  grid: { show: false },
                  yaxis: { show: false },
                  xaxis: { labels: { show: false }, axisTicks: { show: false }, axisBorder: { show: false } },
                }
              } 
              /> 
            }
        </>
    )
 }

 export default Chart;
