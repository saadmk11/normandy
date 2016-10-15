import React, { PropTypes as pt } from 'react';
import FormField from '../form_fields/FormFieldWrapper.js';

export const HeartbeatFormFields = [
  'surveyId',
  'message',
  'engagementButtonLabel',
  'thanksMessage',
  'postAnswerUrl',
  'learnMoreMessage',
  'learnMoreUrl',
];

export default function HeartbeatForm({ fields }) {
  return (
    <div className="row">
      <p className="help row">
        This action can show a single survey, or choose a single survey from
        multiple weighted ones.
      </p>
      <div className="fluid-4">
        <FormField type="text" label="Survey ID" field={fields.surveyId} />
        <FormField label="Message" field={fields.message} />
        <FormField label="Engagement Button Label" field={fields.engagementButtonLabel} />
        <FormField label="Thanks Message" field={fields.thanksMessage} />
        <FormField label="Post Answer Url" field={fields.postAnswerUrl} />
        <FormField label="Learn More Message" field={fields.learnMoreMessage} />
        <FormField label="Learn More Url" field={fields.learnMoreUrl} />
      </div>
    </div>
  );
}
HeartbeatForm.propTypes = {
  fields: pt.object.isRequired,
};
