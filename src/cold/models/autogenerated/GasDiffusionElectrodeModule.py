
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PorousElectrodeModule import PorousElectrode



from .InertElectrodeModule import InertElectrode





from .ConstituentModule import Constituent





class GasDiffusionElectrode(PorousElectrode, InertElectrode):
    """
    Class representing the `GasDiffusionElectrode` entity, which inherits from:
    - PorousElectrode, InertElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bbb1d95b_72d1_44f6_b07e_a3d7d41ac215'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GasDiffusionElectrode'`
        - **Alias**: `class_name`
    
    - `hasConstituent` (`Optional[Constituent]`): 
        - **Default Value**: `None`
        - **Alias**: `hasConstituent`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GasDiffusionElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bbb1d95b_72d1_44f6_b07e_a3d7d41ac215',
    
    class_name='GasDiffusionElectrode',
    
    hasConstituent="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    IEVReference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bbb1d95b_72d1_44f6_b07e_a3d7d41ac215',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GasDiffusionElectrode',
        alias="class_name"
    )
    
    hasConstituent: Optional[Constituent] = Field(
        None,
        alias="hasConstituent"
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
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    @validator("hasConstituent", pre=True, always=True)
    def validate_hasConstituent(cls, value):
        if value is not None and not isinstance(value, Constituent):
            raise ValueError(f"Field 'hasConstituent' must be an instance of 'Constituent' or its subclass.")
        return value
    
    

    

    