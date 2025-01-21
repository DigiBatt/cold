
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysioChemicalQuantityModule import PhysioChemicalQuantity



from .ISQDimensionlessQuantityModule import ISQDimensionlessQuantity







class MolecularPartitionFunction(PhysioChemicalQuantity, ISQDimensionlessQuantity):
    """
    Class representing the `MolecularPartitionFunction` entity, which inherits from:
    - PhysioChemicalQuantity, ISQDimensionlessQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2a971203_58d5_4039_98ce_be7eafb2b14f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MolecularPartitionFunction'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MolecularPartitionFunction(
    
    class_iri='https://w3id.org/emmo#EMMO_2a971203_58d5_4039_98ce_be7eafb2b14f',
    
    class_name='MolecularPartitionFunction',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2a971203_58d5_4039_98ce_be7eafb2b14f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MolecularPartitionFunction',
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
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    