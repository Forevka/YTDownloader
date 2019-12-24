
-- Drop table

-- DROP TABLE public.videos;

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE IF NOT EXISTS public.videos (
	id uuid NOT NULL DEFAULT uuid_generate_v4(),
	"path" text NULL,
	url text NULL,
	batch_id uuid NULL,
	status int2 NULL,
	CONSTRAINT videos_pk PRIMARY KEY (id)
);

