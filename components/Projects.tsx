"use client"
import { projectsData } from "@/lib/data"
import { motion } from "framer-motion"
export default function Projects(){
    return(
            <motion.div
        className="group mb-3 sm:mb-8 last:mb-0"
        >
                <h2 className="text-3xl font-medium capitalize mb-8 text-center">
                    Mes Projets
                </h2>

                {projectsData.map((Projet)=>(
                    <section className="bg-gray-100 max-w-2xl border border-black/5 rounded-lg overflow-hidden sm:pr-8 relative sm:h-80 hover:bg-gray-200 transition sm:group-even:pl-8 dark:text-white dark:bg-white/10 dark:hover:bg-white/20">
                        <div className="pt-4 pb-7 px-5 sm:pl-10 sm:pr-2 sm:pt-10 sm:max-w-[50%] flex flex-col h-full sm:group-even:ml-72">
                            <h3 className="text-2xl font-semibold">{Projet.title}</h3>
                            <p className="mt-2 leading-relaxed text-gray-700 dark:text-white/70">
                                {Projet.title}
                            </p>
                            <ul className="flex flex-wrap mt-4 gap-2 sm:mt-auto">
                                {Projet.tags.map((tag) => (
                                <li
                                    className="bg-black/70 px-3 py-1 text-[0.7rem] uppercase tracking-wider text-white rounded-full dark:text-white/70"
                                >
                                    {tag}
                                </li>
                                ))}
                            </ul>
                        </div>
                    </section>
                ))}
            </motion.div>
        );
}