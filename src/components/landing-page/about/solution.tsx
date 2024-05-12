import Detail from "./detail"
import List from "./list"

const Solution = () => {
    return(
        <div className="h-full bg-[#424874] text-white px-[240px] pt-20">
            <h1 className="text-start">Expert Care For Your Garden Beauties</h1>
            <h1 className="text-6xl text-start font-semibold pt-4">Revive Your Plants</h1>
            <h1 className="text-start text-4xl font-semibold pt-4">With Proven Solutions</h1>
            <List />
            <Detail />
        </div>
    )
}
export default Solution
