
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ActiveElectrodeModule import ActiveElectrode



from .ElectrodeModule import Electrode





from .MolecularEntityModule import MolecularEntity





class InsertionElectrode(ActiveElectrode, Electrode):
    """
    Class representing the `InsertionElectrode` entity, which inherits from:
    - ActiveElectrode, Electrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_757eae08_4d43_42d4_8b4e_8a0bfd2f9a1c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'InsertionElectrode'`
        - **Alias**: `class_name`
    
    - `hasInsertedEntity` (`Optional[MolecularEntity]`): 
        - **Default Value**: `None`
        - **Alias**: `hasInsertedEntity`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = InsertionElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_757eae08_4d43_42d4_8b4e_8a0bfd2f9a1c',
    
    class_name='InsertionElectrode',
    
    hasInsertedEntity="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_757eae08_4d43_42d4_8b4e_8a0bfd2f9a1c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'InsertionElectrode',
        alias="class_name"
    )
    
    hasInsertedEntity: Optional[MolecularEntity] = Field(
        None,
        alias="hasInsertedEntity"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    @validator("hasInsertedEntity", pre=True, always=True)
    def validate_hasInsertedEntity(cls, value):
        if value is not None and not isinstance(value, MolecularEntity):
            raise ValueError(f"Field 'hasInsertedEntity' must be an instance of 'MolecularEntity' or its subclass.")
        return value
    
    

    

    