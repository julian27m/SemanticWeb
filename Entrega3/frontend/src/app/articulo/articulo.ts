export class Articulo {
    id: number;
    nombre: string;
    ruta_pdf: string;
    autor_id?: number;
    nombre_autor?: string;
    referencias?: string;  // Nuevo atributo para referencias
    abstract?: string;
    introduction?: string;
    keywords?: string;
    citation_velocity?: string;
    doi?: number;
    venue?: string;
    anio?: number;
    oppen_access?: boolean;
    licensed?: boolean;


    public constructor(id: number, nombre: string, ruta_pdf: string, autor_id: number, nombre_autor: string, referencias?: string, introduction?: string, abstract?: string, keywords?: string, citation_velocity?: string, doi?: number, venue?: string ,oppen_access?: boolean ,licensed?: boolean ,anio?: number) {
        this.id = id;
        this.nombre = nombre;
        this.ruta_pdf = ruta_pdf;
        this.autor_id = autor_id;
        this.nombre_autor = nombre_autor;
        this.referencias = referencias;
        this.abstract = abstract;
        this.introduction = introduction;
        this.keywords = keywords;
        this.citation_velocity = citation_velocity;
        this.doi = doi;
        this.venue = venue;
        this.anio = anio;
        this.oppen_access = oppen_access;
        this.licensed = licensed;
    }
}
