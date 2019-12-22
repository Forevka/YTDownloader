import { IFile } from "../IFile";
import { IQuality } from '../IQuality';

export interface ResponseFileInterface {
    file: IFile
}

export interface ResponseQualitysInterface {
    quality_list: IQuality[];
}