export class Question {
    constructor(
      public id: number,
      public address: string,
      public body: string,
      public city?: string,
    ) {  }
  }