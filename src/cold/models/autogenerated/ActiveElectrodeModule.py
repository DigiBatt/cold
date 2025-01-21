
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrodeModule import Electrode



from .WholeModule import Whole



from .ElectrochemicalConstituentModule import ElectrochemicalConstituent





from .ConstituentModule import Constituent





class ActiveElectrode(Electrode, Whole, ElectrochemicalConstituent):
    """
    Class representing the `ActiveElectrode` entity, which inherits from:
    - Electrode, Whole, ElectrochemicalConstituent

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9a823d64_9d10_4a29_9cbd_9bbdad7985bc'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ActiveElectrode'`
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
    obj = ActiveElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9a823d64_9d10_4a29_9cbd_9bbdad7985bc',
    
    class_name='ActiveElectrode',
    
    hasConstituent="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9a823d64_9d10_4a29_9cbd_9bbdad7985bc',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ActiveElectrode',
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
    
    

    

    