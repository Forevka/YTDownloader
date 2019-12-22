import { Guid } from "@/utilities/guid";

export interface IQuality {
    id: Guid;
    name: string;
    description: string;
    bitrate: number;
}
