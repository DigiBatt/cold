
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DiffusionCoefficientModule import DiffusionCoefficient



from .EffectivePorousMediaQuantityModule import EffectivePorousMediaQuantity







class EffectiveDiffusionCoefficient(DiffusionCoefficient, EffectivePorousMediaQuantity):
    """
    Class representing the `EffectiveDiffusionCoefficient` entity, which inherits from:
    - DiffusionCoefficient, EffectivePorousMediaQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1744d51d_0dac_4f48_8b50_fde6c7c2ab39'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'EffectiveDiffusionCoefficient'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = EffectiveDiffusionCoefficient(
    
    class_iri='https://w3id.org/emmo#EMMO_1744d51d_0dac_4f48_8b50_fde6c7c2ab39',
    
    class_name='EffectiveDiffusionCoefficient',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1744d51d_0dac_4f48_8b50_fde6c7c2ab39',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'EffectiveDiffusionCoefficient',
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
    

    
    

    

    