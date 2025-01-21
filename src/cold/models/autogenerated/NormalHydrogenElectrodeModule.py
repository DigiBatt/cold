
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ReferenceElectrodeModule import ReferenceElectrode







class NormalHydrogenElectrode(ReferenceElectrode):
    """
    Class representing the `NormalHydrogenElectrode` entity, which inherits from:
    - ReferenceElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_83ee23b3_2f5c_4afa_b972_ac85e91d7306'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NormalHydrogenElectrode'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NormalHydrogenElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_83ee23b3_2f5c_4afa_b972_ac85e91d7306',
    
    class_name='NormalHydrogenElectrode',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_83ee23b3_2f5c_4afa_b972_ac85e91d7306',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NormalHydrogenElectrode',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    