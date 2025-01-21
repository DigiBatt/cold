
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MaterialTreatmentModule import MaterialTreatment







class FormingBlasting(MaterialTreatment):
    """
    Class representing the `FormingBlasting` entity, which inherits from:
    - MaterialTreatment

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_46f70544_818e_495e_99ef_d342c54ee7dc'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FormingBlasting'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FormingBlasting(
    
    class_iri='https://w3id.org/emmo#EMMO_46f70544_818e_495e_99ef_d342c54ee7dc',
    
    class_name='FormingBlasting',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_46f70544_818e_495e_99ef_d342c54ee7dc',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FormingBlasting',
        alias="class_name"
    )
    

    
    

    

    