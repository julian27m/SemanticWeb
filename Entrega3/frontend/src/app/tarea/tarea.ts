export class Tarea {
  id: number;
  texto: string;
  fechaInicial: string;
  fechaFinal: string;
  estado: string;

  public constructor(id: number, texto: string, fechaInicial: string, fechaFinal: string, estado: string) {
    this.id = id;
    this.texto = texto;
    this.fechaInicial = fechaInicial;
    this.fechaFinal = fechaFinal;
    this.estado = estado;
  }

}
