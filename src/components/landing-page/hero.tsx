import { Button } from "../ui/button"

const Hero = () => {
    return (
        <div className="w-full h-[720px] bg-[#150851] px-[240px]">
            <h1 className="text-white text-justify text-6xl pt-10 font-semibold">Revitalize Your Garden with Expert Plant Care and Disease Solutions</h1>
            <div className="flex mt-10 gap-x-4">
            <Button >Get Started</Button>
            <a href="/about" className="text-white mt-2 text-center">Learn more</a>
            </div>
        </div>
    )
}
export default Hero
