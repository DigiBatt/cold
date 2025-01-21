
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WholeModule import Whole



from .ElectrochemicalConstituentModule import ElectrochemicalConstituent





from .ConstituentModule import Constituent





class ActiveMaterialMix(Whole, ElectrochemicalConstituent):
    """
    Class representing the `ActiveMaterialMix` entity, which inherits from:
    - Whole, ElectrochemicalConstituent

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_81833d8a_b03d_4250_be84_6385415beb01'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ActiveMaterialMix'`
        - **Alias**: `class_name`
    
    - `hasConstituent` (`Optional[Constituent]`): 
        - **Default Value**: `None`
        - **Alias**: `hasConstituent`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ActiveMaterialMix(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_81833d8a_b03d_4250_be84_6385415beb01',
    
    class_name='ActiveMaterialMix',
    
    hasConstituent="example_value",
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_81833d8a_b03d_4250_be84_6385415beb01',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ActiveMaterialMix',
        alias="class_name"
    )
    
    hasConstituent: Optional[Constituent] = Field(
        None,
        alias="hasConstituent"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    @validator("hasConstituent", pre=True, always=True)
    def validate_hasConstituent(cls, value):
        if value is not None and not isinstance(value, Constituent):
            raise ValueError(f"Field 'hasConstituent' must be an instance of 'Constituent' or its subclass.")
        return value
    
    

    

    