
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .HeatTreatmentModule import HeatTreatment







class PrecipitationHardening(HeatTreatment):
    """
    Class representing the `PrecipitationHardening` entity, which inherits from:
    - HeatTreatment

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3c7affee_09ed_42e7_a190_4a10c75ab6dd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PrecipitationHardening'`
        - **Alias**: `class_name`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PrecipitationHardening(
    
    class_iri='https://w3id.org/emmo#EMMO_3c7affee_09ed_42e7_a190_4a10c75ab6dd',
    
    class_name='PrecipitationHardening',
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3c7affee_09ed_42e7_a190_4a10c75ab6dd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PrecipitationHardening',
        alias="class_name"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    