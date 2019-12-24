
-- Drop table

-- DROP TABLE public.videos;

CREATE TABLE public.videos (
	id uuid NOT NULL DEFAULT uuid_generate_v4(),
	"path" text NULL,
	url text NULL,
	bath_id uuid NOT NULL DEFAULT uuid_generate_v4()
);
