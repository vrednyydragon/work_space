import Link from "next/link";
import {signOut} from "next-auth/react";

const Navbar = () => {

    return (
        <nav
            className="font-sans flex flex-col text-center sm:flex-row sm:text-left sm:justify-between py-4 px-6 bg-slate-700 shadow sm:items-baseline w-full">
            <div className="mb-2 sm:mb-0">
                <Link href="/">
                    <a className="text-2xl no-underline text-white hover:text-blue-dark">Home</a>
                </Link>
            </div>
            <div>
                <a className="text-lg no-underline text-white hover:text-blue-dark hover:cursor-pointer"
                   onClick={() => signOut()}>Logout</a>
            </div>
        </nav>
    )
}

export default Navbar
