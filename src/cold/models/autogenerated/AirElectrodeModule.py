
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GasDiffusionElectrodeModule import GasDiffusionElectrode





from .ConstituentModule import Constituent





class AirElectrode(GasDiffusionElectrode):
    """
    Class representing the `AirElectrode` entity, which inherits from:
    - GasDiffusionElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8b40856f_1ca2_4137_9616_7fb624671909'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AirElectrode'`
        - **Alias**: `class_name`
    
    - `hasConstituent` (`Optional[Constituent]`): 
        - **Default Value**: `None`
        - **Alias**: `hasConstituent`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AirElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8b40856f_1ca2_4137_9616_7fb624671909',
    
    class_name='AirElectrode',
    
    hasConstituent="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8b40856f_1ca2_4137_9616_7fb624671909',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AirElectrode',
        alias="class_name"
    )
    
    hasConstituent: Optional[Constituent] = Field(
        None,
        alias="hasConstituent"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    @validator("hasConstituent", pre=True, always=True)
    def validate_hasConstituent(cls, value):
        if value is not None and not isinstance(value, Constituent):
            raise ValueError(f"Field 'hasConstituent' must be an instance of 'Constituent' or its subclass.")
        return value
    
    

    

    