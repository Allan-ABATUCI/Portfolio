"use client";

import { projectsData } from "@/lib/data";
import Project from "@/components/Project";
import { useSectionInView } from "@/lib/hooks";

export default function Projects() {
  const { ref } = useSectionInView("Projets", 0.5);

  return (
    <section ref={ref} id="projects" className="scroll-mt-28 mb-28">
      <h2 className="text-3xl font-medium capitalize mb-8 text-center">Mes Projets</h2>
        {projectsData.map((project,index) => (
           
            <Project {...project} key={index}/>

        ))}

    </section>
  );
}