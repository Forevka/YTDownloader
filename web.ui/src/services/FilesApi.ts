import axios, { AxiosStatic } from 'axios';
import { IFile } from '@/models/IFile';
import {ResponseFileInterface} from '@/models/responses/ResponseFile';

export class FilesApi {
    private static filesAxios = axios.create();

    static async getFile(link_to_video: string): Promise<IFile> {
        let url = 'http://forevka.free.beeceptor.com/api/v1/file?youtube.com'
        let response = await this.filesAxios.get<ResponseFileInterface>(url);
        return response.data.file;
    }
}