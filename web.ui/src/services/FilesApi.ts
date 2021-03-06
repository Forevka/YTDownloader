import axios, { AxiosStatic } from 'axios';
import { IFile } from '@/models/IFile';
import { ResponseFileInterface, ResponseQualitysInterface } from '@/models/responses/ResponseFile';
import { IQuality } from '@/models/IQuality';
import { Guid } from '@/utilities/guid';

export class FilesApi {
    private static filesAxios = axios.create();

    static async getFile(link_to_video: string): Promise<IFile> {
        let url = 'http://forevka.free.beeceptor.com/api/v1/file?youtube.com'
        let response = await this.filesAxios.get<ResponseFileInterface>(url);
        return response.data.file;
    }

    static async getAvailableQuality(): Promise<IQuality[]> {
        //let url = 'http://forevka.free.beeceptor.com/api/v1/file?youtube.com'

        let resp_dict = {
            quality_list: [
                {
                    id: new Guid("2c7725bc-77c0-4e1f-b357-b02c2f93887d"),
                    name: "Good",
                    description: "Good one",
                    bitrate: 256
                },
                {
                    id: new Guid("d9250a73-8cef-4f76-9b25-6e6f0afa2923"),
                    name: "Normal",
                    description: "Normal one",
                    bitrate: 128
                },
                {
                    id: new Guid("cff61813-0a29-4245-ac12-270113486192"),
                    name: "Bad",
                    description: "Bad one",
                    bitrate: 64
                },
            ]
        }

        //let response = //await this.filesAxios.get<ResponseQualitysInterface>(url);
        return resp_dict.quality_list;
    }
}