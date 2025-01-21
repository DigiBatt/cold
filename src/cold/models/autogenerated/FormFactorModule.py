
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .InformationModule import Information







class FormFactor(Information):
    """
    Class representing the `FormFactor` entity, which inherits from:
    - Information

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1586ef26_6d30_49e3_ae32_b4c9fc181941'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FormFactor'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FormFactor(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1586ef26_6d30_49e3_ae32_b4c9fc181941',
    
    class_name='FormFactor',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1586ef26_6d30_49e3_ae32_b4c9fc181941',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FormFactor',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    