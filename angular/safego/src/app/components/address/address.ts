export class Address{
    constructor(
        public id: number,
        public address: string,
        public city?: string,
        public risk?: string,
      ) {  }
  }