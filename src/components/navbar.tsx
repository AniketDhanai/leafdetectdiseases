import { Button } from "./ui/button"

const Navbar = () => {
    return (
        <nav className="w-full h-[70px] bg-[#424874] flex items-center justify-between px-[120px]">
            <div className="text-white font-semibold">Leaf Healer</div>
            <div>
                <ul className="flex space-x-4">
                    <li className="text-white">Home</li>
                    <li className="text-white">Diseases</li>
                    <li className="text-white">Plants</li>
                </ul>
            </div>
            <div>
                <Button>Get Started</Button>
            </div>
        </nav>
    )
}
export default Navbar
