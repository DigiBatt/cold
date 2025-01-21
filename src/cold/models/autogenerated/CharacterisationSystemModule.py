
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .HolisticSystemModule import HolisticSystem



from .MeasuringSystemModule import MeasuringSystem





from .ConstituentModule import Constituent





class CharacterisationSystem(HolisticSystem, MeasuringSystem):
    """
    Class representing the `CharacterisationSystem` entity, which inherits from:
    - HolisticSystem, MeasuringSystem

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationSystem'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CharacterisationSystem'`
        - **Alias**: `class_name`
    
    - `definition` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `definition`
    
    - `hasConstituent` (`Optional[Constituent]`): 
        - **Default Value**: `None`
        - **Alias**: `hasConstituent`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `VIMTerm` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `VIMTerm`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CharacterisationSystem(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationSystem',
    
    class_name='CharacterisationSystem',
    
    definition="example_value",
    
    hasConstituent="example_value",
    
    elucidation="example_value",
    
    VIMTerm="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationSystem',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CharacterisationSystem',
        alias="class_name"
    )
    
    definition: Optional[str] = Field(
        None,
        alias="definition"
    )
    
    hasConstituent: Optional[Constituent] = Field(
        None,
        alias="hasConstituent"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    VIMTerm: Optional[str] = Field(
        None,
        alias="VIMTerm"
    )
    

    
    @validator("hasConstituent", pre=True, always=True)
    def validate_hasConstituent(cls, value):
        if value is not None and not isinstance(value, Constituent):
            raise ValueError(f"Field 'hasConstituent' must be an instance of 'Constituent' or its subclass.")
        return value
    
    

    

    